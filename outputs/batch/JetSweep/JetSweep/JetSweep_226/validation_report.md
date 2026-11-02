# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_226`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_226/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 60 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '6' (C): higher_priority='Action_BallSnap' [63–74], lower_priority='Action_ZoneBlock' annotated_start=65, effective_Action_ZoneBlock_start=75.
> - Action 'Action_ZoneBlock' range [65-118] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-168] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [63-115] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-138] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-212] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-129] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-127] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-76] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-113] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-124] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [65-128] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [65-134] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-138] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [92-195] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-119] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-82] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-239] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-221] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [149-161] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-181] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [184-197] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-232] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-237] for track '27' has 1 frames without a visible bounding box.
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
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.