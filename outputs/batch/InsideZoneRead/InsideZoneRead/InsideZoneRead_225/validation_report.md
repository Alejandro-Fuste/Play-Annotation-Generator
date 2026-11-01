# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `InsideZoneRead_225`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_225/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 0 |
| Action Segments inferred | 46 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Row 226, Column 'Pre Snap': Could not parse frame number from '-' in entry '-,ALL'.
> - Row 226, Column 'Zone Block': Could not parse frame number from '-' in entry '-,OL'.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 450: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [0-325] for track '0' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-230] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-329] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-173] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-329] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-260] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-178] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-214] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-255] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-329] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-329] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-207] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-177] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-278] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-329] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-131] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-166] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-254] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-162] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-39] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-53] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-69] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-171] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-225] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-256] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-280] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [285-297] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [302-303] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [324-328] for track '29' has 2 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Play definition: no definition found for 'Play_Unknown'.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.