# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_45`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_45/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 59 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 70: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [68–75], lower_priority='Action_RunBlock' annotated_start=75, effective_Action_RunBlock_start=76.
> - Action 'Action_None' range [68-138] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-208] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_SecureCatch' range [206-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-103] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-128] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-210] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [68-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-210] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [68-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [76-210] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [75-100] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [103-106] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [75-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [75-108] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [75-136] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [138-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-208] for track '24' has 1 frames without a visible bounding box.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.