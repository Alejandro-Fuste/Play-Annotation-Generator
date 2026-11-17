# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_56`
- **Input XML**: `outputs/batch/Power/Power/Power_56/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 23 |
| Player Tracks | 23 |
| Ball Tracks | 0 |
| CSV events parsed | 9 |
| Action Segments inferred | 44 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 114: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - Row 114: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - Track ID '17' in Player Track ID sheet does not exist in MOT gt.txt.
> - Track ID '14' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_PreSnap' range [25-205] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-172] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-269] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [106-117] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-182] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-212] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-224] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-114] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-129] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-171] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-174] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-182] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-269] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-241] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-254] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-162] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-167] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-218] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-264] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-242] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-189] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-269] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-269] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-181] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-269] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-223] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-233] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-233] for track '22' has 1 frames without a visible bounding box.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.