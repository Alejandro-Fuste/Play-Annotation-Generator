# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_229`
- **Input XML**: `outputs/batch/Power/Power/Power_229/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 54 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 460: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [8-317] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [152-181] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-214] for track '3' has 7 frames without a visible bounding box.
> - Action 'Action_None' range [229-230] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-329] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-257] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-163] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-208] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-259] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-216] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-329] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [152-157] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [159-181] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-233] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-189] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-240] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-246] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-189] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-169] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-173] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-178] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-195] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-250] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-169] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-227] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [230-329] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-308] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-51] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-221] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-299] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [302-329] for track '24' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.