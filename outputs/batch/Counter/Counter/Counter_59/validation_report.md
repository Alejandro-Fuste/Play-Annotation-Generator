# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_59`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_59/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 50 |
| Player Tracks | 50 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 151 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 120: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '3' (LT) duration 95 frames exceeds threshold 90 frames [start=180, end=274].
> - Validation warning: Action 'Action_DownBlock' for track '10' (LG) duration 95 frames exceeds threshold 90 frames [start=180, end=274].
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [177–194], lower_priority='Action_DownBlock' annotated_start=180, effective_Action_DownBlock_start=195.
> - Action 'Action_PullLeadBlock' range [180-225] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [219-245] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-241] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-247] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-254] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-79] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-179] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [180-196] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [205-234] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [236-250] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-284] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-295] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-382] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [385-390] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [393-419] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-228] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-240] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-256] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-374] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [379-393] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-255] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-317] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-333] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-200] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-299] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-323] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [177-350] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [177-328] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-361] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [180-189] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [197-274] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [357-410] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-176] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [177-234] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-247] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [177-313] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [327-419] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [177-360] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [195-234] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [237-240] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [244-250] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [177-233] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-288] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [291-313] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [177-225] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-228] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-293] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [295-419] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-224] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-228] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-79] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-83] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [180-233] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [237-241] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-77] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-229] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [236-247] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [249-250] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-263] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-268] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-272] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-308] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-188] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-398] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-235] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-270] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [304-305] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-273] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-273] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-282] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-295] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-286] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-296] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-310] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-313] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-419] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [282-285] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-294] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-297] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-318] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-332] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-296] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-363] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [289-312] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-317] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-321] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [340-357] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [359-374] for track '31' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [379-396] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-411] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [296-300] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-325] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [367-408] for track '33' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [303-311] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-357] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-419] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-357] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [360-364] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [345-346] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-382] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [386-387] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-357] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-385] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [389-392] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [397-399] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [408-411] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-362] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [364-367] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [370-411] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [415-418] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [390-396] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [399-405] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [393-394] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [403-405] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [410-411] for track '48' has 1 frames without a visible bounding box.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.
> - Player track '46' has undefined position. Will map to Position_Unknown.
> - Player track '46' has undefined team_side. Will map to Team_Unknown.
> - Player track '47' has undefined position. Will map to Position_Unknown.
> - Player track '47' has undefined team_side. Will map to Team_Unknown.
> - Player track '48' has undefined position. Will map to Position_Unknown.
> - Player track '48' has undefined team_side. Will map to Team_Unknown.
> - Player track '49' has undefined position. Will map to Position_Unknown.
> - Player track '49' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.