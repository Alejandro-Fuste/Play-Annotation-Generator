# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_241`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_241/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 52 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 484: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_BlockSecondLevel' for track '18' has invalid range: start=182, end=163. Clamping end to start.
> - Action 'Action_PreSnap' range [0-235] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-185] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-194] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [128-157] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-239] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-170] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-202] for track '5' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-165] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-193] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-203] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-239] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-167] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-189] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-169] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-239] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '10' starts at frame 176, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [176-176] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-208] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-207] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-239] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-238] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [128-137] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [149-153] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [165-167] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-127] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-176] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-208] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-220] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-224] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [128-167] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [182-193] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-117] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-163] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-165] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-239] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-239] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-239] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-191] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-239] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-239] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-229] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-236] for track '25' has 2 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.