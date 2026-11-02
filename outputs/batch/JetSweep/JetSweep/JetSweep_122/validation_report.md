# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_122`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_122/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 25 |
| Action Segments inferred | 72 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [87–99], lower_priority='Action_ZoneBlock' annotated_start=89, effective_Action_ZoneBlock_start=100.
> - Action 'Action_None' range [87-215] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-235] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [89-147] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [89-156] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [87-234] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-132] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-194] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [89-149] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [151-153] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [89-132] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [117-230] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-251] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [87-92] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [94-99] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [100-101] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [117-148] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [150-156] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [89-112] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [115-119] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-99] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-197] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-146] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-246] for track '25' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.