# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Dagger_34`
- **Input XML**: `outputs/batch/Dagger/Dagger/Dagger_34/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Dagger.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 21 |
| Player Tracks | 21 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 67 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [139–143], lower_priority='Action_PassBlock' annotated_start=142, effective_Action_PassBlock_start=144.
> - Segment 'Action_ThrowPass' for track '12' has invalid range: start=232, end=220. Clamping end to start.
> - Action 'Action_None' range [139-173] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-167] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-173] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-191] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-182] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-296] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_BreakInside' range [158-278] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-290] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [293-294] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-299] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-259] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-263] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-299] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-138] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [144-146] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [150-152] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [154-155] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-299] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-10] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-18] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-161] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-8] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-16] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-27] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-32] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-138] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-174] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-220] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-18] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-138] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-33] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-56] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-77] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-100] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-126] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ClearToEdge' for track '15' starts at frame 158, but the player has no visible bounding box on this frame.
> - Action 'Action_ClearToEdge' range [158-160] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-173] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-188] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-225] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-186] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-286] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [178-187] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-193] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [269-270] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-287] for track '20' has 1 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.