# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `RPO_234`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_234/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 45 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - RPO Run Block requires exactly five verified OL positions ['C', 'LG', 'LT', 'RG', 'RT']; found ['C', 'LG', 'LT', 'RT'].

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 426: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_PreSnap' range [0-122] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-117] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-255] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-116] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-126] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-69] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-130] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-131] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-76] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-123] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-115] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-126] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-77] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-110] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-123] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-127] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-101] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-122] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-95] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-120] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-104] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-112] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-115] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-116] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-147] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-226] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-165] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-214] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-269] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-268] for track '25' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.