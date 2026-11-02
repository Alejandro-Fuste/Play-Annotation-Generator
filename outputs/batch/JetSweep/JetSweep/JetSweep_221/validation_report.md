# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_221`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_221/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 106 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 444: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [49–62], lower_priority='Action_ZoneBlock' annotated_start=51, effective_Action_ZoneBlock_start=63.
> - Action 'Action_None' range [49-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-130] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-136] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-173] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-178] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-205] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [51-60] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [63-137] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [138-149] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [78-140] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [174-175] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [51-73] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [80-92] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [96-115] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-153] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-210] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [49-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-200] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-165] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [167-210] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [49-132] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-138] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-145] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-63] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-115] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-144] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [147-148] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-191] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [49-145] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [147-171] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [49-137] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-157] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-186] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-210] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [51-63] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-203] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-83] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-139] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-144] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-148] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-77] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [51-61] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [63-67] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-70] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-30] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '21' starts at frame 49, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [49-49] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-144] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-139] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-207] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-146] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [148-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-165] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-178] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [207-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-147] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-154] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-209] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-188] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-200] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-209] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '29' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.