# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_10`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_10/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 27 |
| Action Segments inferred | 66 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [99–102], lower_priority='Action_ZoneBlock' annotated_start=91, effective_Action_ZoneBlock_start=103.
> - Action 'Action_None' range [99-149] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-179] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [91-127] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [91-138] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [143-161] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-166] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-112] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-140] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [91-144] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [150-153] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-176] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-239] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-239] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-97] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-163] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-172] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-37] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-90] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-139] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-169] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [88-112] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [113-169] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-118] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-126] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-129] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-162] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-169] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-232] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-207] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [209-229] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-197] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-216] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-214] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [221-235] for track '25' has 1 frames without a visible bounding box.
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