# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_299`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_299/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 78 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 600: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [108–118], lower_priority='Action_ZoneBlock' annotated_start=116, effective_Action_ZoneBlock_start=119.
> - Action 'Action_None' range [108-202] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-239] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-109] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [150-157] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [164-231] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-178] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-183] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-163] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-206] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-113] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [115-171] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-214] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [108-124] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-141] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-147] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-172] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-192] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-224] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-101] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-104] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-107] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [108-113] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-201] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-206] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [116-154] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [116-157] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-173] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-204] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-235] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-73] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-134] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-139] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-148] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-179] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-202] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-193] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-202] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-236] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-238] for track '22' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.