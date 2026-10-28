# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_96`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_96/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 40 |
| Player Tracks | 40 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 115 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 191: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_PassBlock' for track '15' has invalid range: start=32, end=28. Clamping end to start.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [29–42], lower_priority='Action_PassBlock' annotated_start=32, effective_Action_PassBlock_start=43.
> - Action 'Action_None' range [29-210] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [29-181] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-190] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-202] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-125] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-114] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-210] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [29-85] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [29-67] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-172] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-178] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-135] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-144] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-210] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [29-125] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [131-210] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [29-118] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-157] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-172] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-179] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-184] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-210] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [29-178] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-184] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [87-127] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [139-141] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [144-151] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [153-160] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [167-168] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-47] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-111] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-146] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-165] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-172] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-179] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-151] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-161] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-170] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [43-109] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [32-50] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [53-56] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [59-70] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [77-120] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-165] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [167-169] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-210] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [68-69] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-116] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-131] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-204] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [207-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-126] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-154] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-169] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-186] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-202] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-208] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-136] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-168] for track '28' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [171-177] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-183] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-191] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-196] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-148] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-168] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-158] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [151-152] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-167] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-178] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-210] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-175] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-186] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-177] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-210] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-197] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-210] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-210] for track '39' has 1 frames without a visible bounding box.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.