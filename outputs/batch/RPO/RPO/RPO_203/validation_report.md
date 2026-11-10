# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `RPO_203`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_203/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 66 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - RPO Run Block requires exactly five verified OL positions ['C', 'LG', 'LT', 'RG', 'RT']; found ['C', 'LG', 'LT', 'RG'].

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 376: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_PreSnap' range [0-192] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-142] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-255] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-258] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-267] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-265] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-147] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-187] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [189-192] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-216] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-170] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-173] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-179] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-182] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-203] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-234] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-259] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-265] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-236] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-239] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-248] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-256] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-266] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-123] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-177] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-250] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-133] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-237] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-248] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-256] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-265] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-136] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-185] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-195] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-205] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-208] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-190] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-179] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-177] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-181] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-189] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-267] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-248] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-260] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-263] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-266] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-269] for track '30' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.