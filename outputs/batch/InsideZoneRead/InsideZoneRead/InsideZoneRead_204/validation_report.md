# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_204`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_204/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 84 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 408: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '12' (LT) duration 94 frames exceeds threshold 90 frames [start=94, end=187].
> - Validation warning: Action 'Action_ZoneBlock' for track '18' (RT) duration 94 frames exceeds threshold 90 frames [start=94, end=187].
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [91–105], lower_priority='Action_ZoneBlock' annotated_start=94, effective_Action_ZoneBlock_start=106.
> - Validation warning: Action 'Action_ZoneBlock' for track '21' (RG) duration 94 frames exceeds threshold 90 frames [start=94, end=187].
> - Action 'Action_None' range [91-154] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-158] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-172] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-192] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-196] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-208] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [210-211] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-156] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-162] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-165] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-176] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-235] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [91-182] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [185-236] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [91-224] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-228] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-218] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-230] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_Handoff' for track '14' starts at frame 121, but the player has no visible bounding box on this frame.
> - Action 'Action_Handoff' range [121-132] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-163] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-208] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [94-104] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [135-138] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [94-113] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [138-147] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [158-161] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [164-165] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [170-180] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [182-187] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-201] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-206] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-223] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [106-149] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [94-105] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [109-187] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-6] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-239] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-239] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [220-221] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-227] for track '26' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.