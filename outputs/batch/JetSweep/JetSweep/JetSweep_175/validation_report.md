# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_175`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_175/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 85 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '6' (C): higher_priority='Action_BallSnap' [135–148], lower_priority='Action_ZoneBlock' annotated_start=137, effective_Action_ZoneBlock_start=149.
> - Action 'Action_None' range [135-222] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-236] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [137-182] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [186-214] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [157-235] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-205] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [137-225] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [226-237] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [137-179] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [181-192] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [197-199] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-258] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-272] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-288] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-233] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-259] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [261-265] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-216] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [218-299] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-176] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [178-184] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [135-176] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-221] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [224-232] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [137-181] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-8] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-154] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-295] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-227] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-240] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-242] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-270] for track '28' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [249-260] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [264-265] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-275] for track '30' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.