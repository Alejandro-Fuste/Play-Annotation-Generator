# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_149`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_149/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 25 |
| Action Segments inferred | 74 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [94–107], lower_priority='Action_ZoneBlock' annotated_start=96, effective_Action_ZoneBlock_start=108.
> - Action 'Action_BallCarry' range [120-238] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-234] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [94-192] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [195-197] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-237] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-126] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-130] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-190] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [199-202] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-239] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [96-171] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-200] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-211] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-126] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [108-128] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '15' starts at frame 182, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [182-239] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [94-220] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [94-114] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-118] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-122] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [96-120] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-239] for track '24' has 2 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.