# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `RPO_198`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_198/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 62 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - RPO Run Block requires exactly five verified OL positions ['C', 'LG', 'LT', 'RG', 'RT']; found ['LG', 'LT', 'RG', 'RT'].

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 366: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-138] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-91] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-143] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-98] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-53] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-86] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-91] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-96] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-100] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-103] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-122] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-127] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-156] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-210] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-62] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-46] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-87] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-91] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-122] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-210] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-89] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-96] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-107] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-30] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-84] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-39] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-43] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-49] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-118] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-122] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-117] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-170] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-113] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-142] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-119] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-128] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-173] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-161] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-133] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-136] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-149] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-192] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-201] for track '27' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.