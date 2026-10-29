# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_97`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_97/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 55 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 388 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 196: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 388 as fallback play end.
> - Segment 'Action_ComboBlock' for track '11' has invalid range: start=245, end=239. Clamping end to start.
> - Action 'Action_PreSnap' range [0-245] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-250] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-255] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-346] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-302] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-264] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-326] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-288] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-293] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [245-297] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-310] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [313-327] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-354] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [365-369] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-316] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-324] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [329-330] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [353-365] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [367-369] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [372-388] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-342] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [358-359] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-335] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-269] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-353] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [356-357] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [359-360] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [364-365] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-248] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-253] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-301] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [324-327] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [331-362] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [365-388] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-361] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-307] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [341-348] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-249] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-283] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [290-388] for track '23' has 3 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.