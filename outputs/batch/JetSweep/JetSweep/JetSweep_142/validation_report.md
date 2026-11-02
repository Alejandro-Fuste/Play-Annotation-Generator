# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_142`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_142/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 63 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [23–40], lower_priority='Action_ZoneBlock' annotated_start=25, effective_Action_ZoneBlock_start=41.
> - Action 'Action_None' range [23-96] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-110] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-179] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-194] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-203] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [25-52] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [89-96] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [25-83] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-205] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-82] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [25-88] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-54] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-145] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [147-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-90] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-103] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '12' starts at frame 56, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [56-86] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [41-73] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [77-80] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [82-86] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_SealBlock' range [25-86] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_SealBlock' range [89-133] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [56-197] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [201-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-94] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-117] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-148] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-74] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-113] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-117] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-121] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-181] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-200] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-197] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-210] for track '26' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.