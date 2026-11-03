# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `StopAndGo_43`
- **Input XML**: `outputs/batch/StopAndGo/StopAndGo/StopAndGo_43/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/StopAndGo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 42 |
| Player Tracks | 42 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 138 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [10–14], lower_priority='Action_PassBlock' annotated_start=13, effective_Action_PassBlock_start=15.
> - Action 'Action_None' range [10-62] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-105] for track '0' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [109-110] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-124] for track '0' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [128-146] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-151] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-160] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-107] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-212] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [216-225] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-115] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-179] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-138] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-149] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-162] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-169] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [93-239] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-106] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-126] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-138] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-131] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-145] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [13-122] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [124-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [13-52] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [59-60] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-66] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-106] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-56] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [58-66] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-105] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [108-239] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [13-169] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [176-178] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [13-152] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [158-166] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [174-177] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [191-232] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_ThrowPass' range [111-122] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-152] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-161] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-179] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-22] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-35] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-58] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-77] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-84] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-96] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-163] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-169] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-75] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-78] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-99] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-118] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [100-126] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-161] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-166] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-181] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-186] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-203] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [209-211] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-217] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-120] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-150] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [154-160] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-141] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-153] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-166] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-207] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [134-135] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-146] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-149] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-155] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-162] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-169] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-177] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [185-186] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-211] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-234] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-174] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [162-163] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-168] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-173] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-186] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-212] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-227] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [236-239] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [186-188] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-199] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-220] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-230] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-239] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-213] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [217-219] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-230] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-224] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [226-235] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [218-221] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-230] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-224] for track '41' has 1 frames without a visible bounding box.
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
> - Play definition: no definition found for 'Play_Pass_StopAndGo'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.