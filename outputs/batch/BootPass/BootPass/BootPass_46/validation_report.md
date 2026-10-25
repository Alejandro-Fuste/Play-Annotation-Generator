# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_46`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_46/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 30 |
| Ball Tracks | 1 |
| CSV events parsed | 21 |
| Action Segments inferred | 71 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 72: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [87–94], lower_priority='Action_RunBlock' annotated_start=94, effective_Action_RunBlock_start=95.
> - Action 'Action_None' range [87-137] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-141] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-154] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-160] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-225] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [229-239] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-114] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-140] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-162] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [94-104] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [107-108] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [120-127] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [130-158] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [94-168] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [94-119] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [130-165] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [87-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-138] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-227] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [95-130] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-138] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-111] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-144] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-134] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-139] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [87-92] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '20' starts at frame 95, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [95-120] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BootAway' range [121-171] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-208] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-122] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-137] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-130] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-236] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_RunFlatRoute' range [150-153] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-239] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '29' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.