# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Hitch_60`
- **Input XML**: `outputs/batch/Hitch/Hitch/Hitch_60/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Hitch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 38 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 185 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 70: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [2–6], lower_priority='Action_PassBlock' annotated_start=5, effective_Action_PassBlock_start=7.
> - Action 'Action_None' range [2-59] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-81] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-94] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-175] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [179-191] for track '0' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [200-205] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-215] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-218] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-228] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-232] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-232] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-7] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-82] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-90] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-93] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [138-208] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [212-215] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-208] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-34] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-44] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-98] for track '8' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [2-156] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-215] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [5-16] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-9] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-164] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-194] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-208] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-214] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-218] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-239] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-19] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [31-33] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [37-38] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [72-79] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [88-90] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [92-94] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [96-98] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [104-120] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [124-130] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [132-175] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [180-211] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [213-217] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [220-223] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [5-6] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [70-71] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [73-81] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [92-94] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [96-99] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [103-119] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [122-130] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [140-172] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [177-182] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [184-196] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [204-209] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [212-215] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [218-219] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [221-228] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [5-6] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [18-30] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [66-67] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [70-71] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [73-79] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-4] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [2-4] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-35] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-92] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ThrowPass' range [93-102] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-120] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-130] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-172] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-178] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [182-184] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-192] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-54] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-159] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-179] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [181-189] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-201] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-228] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [230-239] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-55] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-56] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-81] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [88-129] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-145] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-87] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-99] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-130] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-146] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-152] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-158] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-68] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-81] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-123] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [138-173] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-182] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-192] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [74-79] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-99] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-146] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-152] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-161] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-196] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-208] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [212-215] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-145] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-113] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [105-119] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-130] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [114-129] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-146] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [150-161] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [163-173] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [213-228] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-126] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-178] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-185] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-222] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-130] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-148] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [152-161] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [163-167] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-171] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-183] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-192] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-213] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-218] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-231] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-167] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [171-172] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-166] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-172] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-213] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [220-239] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-232] for track '33' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-193] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-208] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-227] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-234] for track '36' has 1 frames without a visible bounding box.
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
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.