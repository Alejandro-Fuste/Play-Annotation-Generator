# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_62`
- **Input XML**: `outputs/batch/Power/Power/Power_62/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 65 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 126: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [28-274] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-286] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-290] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-327] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-221] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-329] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-306] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [309-311] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-141] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-250] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-288] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-292] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-301] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-304] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-313] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-319] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-254] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-279] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-329] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-248] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [270-271] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [277-281] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-249] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-154] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-167] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-203] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [222-240] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [244-257] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [261-264] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [266-267] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [270-290] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-311] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-231] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-246] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-249] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-291] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-215] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-38] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-214] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-227] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-236] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-34] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-245] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [275-276] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [280-281] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [287-288] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-295] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-294] for track '22' has 2 frames without a visible bounding box.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.