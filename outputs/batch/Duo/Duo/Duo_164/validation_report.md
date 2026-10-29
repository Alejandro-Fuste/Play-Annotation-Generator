# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_164`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_164/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 87 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 268 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 268 as fallback play end.
> - Action 'Action_PreSnap' range [0-230] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-260] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-264] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-214] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-223] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-259] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-264] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-113] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-121] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-161] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-181] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [187-193] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [205-207] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [212-226] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [253-264] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-266] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-177] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-268] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-158] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [187-238] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [241-242] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [245-246] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-204] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-215] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-256] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-263] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-268] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-186] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [187-215] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [246-250] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-30] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-35] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-39] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-43] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-80] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-184] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [187-252] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [253-264] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-174] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-183] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-262] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-140] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-146] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-149] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-268] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-25] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-136] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-268] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-66] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-92] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-126] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-177] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-165] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-250] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-254] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-260] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-264] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-209] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-214] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-238] for track '23' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-262] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-194] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-214] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-268] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-241] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-266] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-234] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-252] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-268] for track '29' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.