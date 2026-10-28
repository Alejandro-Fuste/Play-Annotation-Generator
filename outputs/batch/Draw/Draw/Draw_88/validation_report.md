# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_88`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_88/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 128 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 176: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [32–48], lower_priority='Action_PassBlock' annotated_start=35, effective_Action_PassBlock_start=49.
> - Action 'Action_None' range [32-158] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-183] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-239] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-98] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [101-213] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-106] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-97] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-104] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-109] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-123] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-131] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-138] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-149] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-239] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-71] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-92] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-118] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [32-137] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-170] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-218] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [35-74] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [84-85] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [88-107] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-151] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-170] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-195] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-205] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [212-216] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-131] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-239] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [74-91] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [95-97] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [104-202] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [208-239] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-237] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-101] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-194] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-74] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-95] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [49-67] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [70-94] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-120] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-148] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-172] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-201] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-211] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-220] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [225-228] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-238] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-58] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-99] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-117] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-123] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [35-107] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-114] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [35-74] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-157] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [35-58] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [60-90] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-109] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-74] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-111] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [114-115] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-154] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-162] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-115] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-121] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-131] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-140] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-159] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-163] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-170] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-195] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-203] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-207] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-231] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-154] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-216] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [226-227] for track '33' has 1 frames without a visible bounding box.
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