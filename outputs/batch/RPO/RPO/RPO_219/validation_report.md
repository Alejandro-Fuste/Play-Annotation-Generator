# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `RPO_219`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_219/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 56 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - RPO Run Block requires exactly five verified OL positions ['C', 'LG', 'LT', 'RG', 'RT']; found ['C', 'LG', 'RG', 'RT'].

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 408: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_PreSnap' range [0-75] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-93] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-134] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-171] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-212] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-269] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-268] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-144] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-257] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-79] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-143] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-199] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-160] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-157] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-160] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-59] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-135] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-243] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-224] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-230] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [47-178] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-185] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-192] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-138] for track '17' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-57] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-173] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-49] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-66] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-134] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-137] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-165] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-34] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-48] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-151] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-47] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-162] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-60] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-80] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-114] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-131] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-155] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-173] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-194] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-200] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-143] for track '26' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.