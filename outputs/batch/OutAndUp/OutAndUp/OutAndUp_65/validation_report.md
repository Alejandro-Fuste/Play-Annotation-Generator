# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutAndUp_65`
- **Input XML**: `outputs/batch/OutAndUp/OutAndUp/OutAndUp_65/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutAndUp.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 55 |
| Player Tracks | 55 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 168 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '4' (C): higher_priority='Action_BallSnap' [65–70], lower_priority='Action_PassBlock' annotated_start=68, effective_Action_PassBlock_start=71.
> - Action 'Action_None' range [65-220] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [65-287] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [65-110] for track '3' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [119-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-123] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-137] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [71-79] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [97-110] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [65-100] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-107] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-186] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [65-124] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [126-151] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-161] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-168] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-183] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-203] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-211] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-217] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-170] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-202] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-215] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [218-299] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-187] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-193] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-196] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-131] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-138] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-149] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-215] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [222-254] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [68-92] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [94-107] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [65-225] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-229] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-80] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-91] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-107] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [68-89] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [95-96] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [68-74] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [76-84] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-110] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [158-240] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [175-299] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-139] for track '20' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [152-155] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-162] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-177] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-189] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-199] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-218] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-238] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [68-92] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [103-110] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [122-123] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [128-161] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [104-110] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [177-183] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-186] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-196] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-204] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [207-268] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-297] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-146] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-149] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-152] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-196] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-134] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-148] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-153] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-199] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-206] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-151] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-224] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [254-257] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-266] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [268-293] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-297] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-192] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-207] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-195] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-257] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [259-260] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-269] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [274-277] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-282] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-285] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-297] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-239] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-264] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-278] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-221] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-239] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-248] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [250-255] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [264-267] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-230] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-299] for track '32' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [232-243] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-277] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-234] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-239] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-243] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-260] for track '37' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [263-264] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-292] for track '37' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [242-260] for track '38' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [244-246] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-250] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-263] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [265-267] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-253] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-260] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-273] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [275-283] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-296] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-271] for track '43' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [277-299] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-254] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-259] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-265] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-275] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-299] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-263] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-296] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-295] for track '48' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [278-283] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-299] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-286] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-295] for track '53' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [297-299] for track '54' has 1 frames without a visible bounding box.
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
> - Player track '50' has undefined position. Will map to Position_Unknown.
> - Player track '50' has undefined team_side. Will map to Team_Unknown.
> - Player track '51' has undefined position. Will map to Position_Unknown.
> - Player track '51' has undefined team_side. Will map to Team_Unknown.
> - Player track '52' has undefined position. Will map to Position_Unknown.
> - Player track '52' has undefined team_side. Will map to Team_Unknown.
> - Player track '53' has undefined position. Will map to Position_Unknown.
> - Player track '53' has undefined team_side. Will map to Team_Unknown.
> - Player track '54' has undefined position. Will map to Position_Unknown.
> - Player track '54' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.