# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_86`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_86/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 120 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [22–36], lower_priority='Action_PassBlock' annotated_start=25, effective_Action_PassBlock_start=37.
> - Action 'Action_None' range [22-82] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-118] for track '0' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [22-210] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [22-99] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-196] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-106] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-119] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-140] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-157] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-162] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-169] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-177] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-166] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-171] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-194] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [203-209] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-104] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [71-97] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [105-106] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [189-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-34] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-99] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [101-102] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-116] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-124] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [25-35] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [44-55] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [58-87] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [22-33] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [25-35] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [45-67] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [76-78] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-189] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-157] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-163] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-179] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-192] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-201] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-33] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [25-33] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [43-85] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-33] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-55] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-66] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-140] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-79] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [89-118] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [120-154] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-179] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-190] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-208] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [25-33] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [45-56] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [61-79] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [82-85] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-142] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [144-183] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-194] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [22-32] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [45-53] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [60-90] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [92-129] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [134-161] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-67] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-89] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [96-97] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-106] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-87] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-89] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [107-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-133] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-140] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-164] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-157] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-183] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-193] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-210] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [149-153] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [191-210] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-210] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-210] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '35' has 1 frames without a visible bounding box.
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