# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_99`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_99/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 75 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_BallCarry' for track '8' has invalid range: start=128, end=102. Clamping end to start.
> - Action 'Action_None' range [91-214] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-239] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-56] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-74] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-85] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '8' starts at frame 102, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [102-102] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [93-152] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-212] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-158] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [93-111] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [152-157] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '18' starts at frame 167, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [167-167] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-239] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [93-118] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [120-131] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [134-135] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-50] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-62] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-78] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-137] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-227] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-155] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [160-239] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [217-218] for track '27' has 1 frames without a visible bounding box.
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