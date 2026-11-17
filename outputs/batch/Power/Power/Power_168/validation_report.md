# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_168`
- **Input XML**: `outputs/batch/Power/Power/Power_168/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 121 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action 'Action_PreSnap' range [24-233] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-241] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-268] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-276] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [271-296] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-302] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-306] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-334] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [336-339] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-253] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-326] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [328-357] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-72] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-224] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-249] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-306] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-318] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [324-359] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-200] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-240] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-359] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-245] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-284] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-232] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-247] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [275-281] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [285-290] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [195-215] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [221-223] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [225-229] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [234-260] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [262-268] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-290] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-311] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [313-330] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [332-334] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [336-338] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-78] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-93] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-100] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-128] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-146] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-170] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-174] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-212] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-255] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-259] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-299] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [304-340] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [344-354] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [356-357] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [195-199] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [214-215] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-296] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-32] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-36] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-60] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-71] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-85] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-121] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-131] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-175] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-196] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-183] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-254] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-202] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-211] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-221] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-245] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-251] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-229] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-254] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-262] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-271] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [281-284] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-288] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-302] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [308-309] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [315-334] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [336-339] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [341-344] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-231] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-259] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-248] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-359] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-263] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-266] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [308-310] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-299] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [301-303] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-359] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-265] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-274] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [280-282] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-325] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [341-344] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [316-330] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [338-340] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [343-355] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [319-334] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [346-347] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [355-359] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [333-334] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [341-342] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [352-359] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [351-359] for track '35' has 3 frames without a visible bounding box.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.