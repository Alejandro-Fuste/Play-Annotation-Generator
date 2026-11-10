# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `RPO_24`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_24/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 51 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - RPO Run Block requires exactly five verified OL positions ['C', 'LG', 'LT', 'RG', 'RT']; found ['C', 'LT', 'RG', 'RT'].

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-180] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-87] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-173] for track '4' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-63] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-69] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-164] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-111] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-148] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-154] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-148] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-157] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-168] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-111] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-176] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [49-57] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-159] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-55] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-159] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-58] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-65] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-170] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-90] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-43] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-49] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-180] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-77] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-81] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-100] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-116] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-120] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-157] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-166] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-174] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-179] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-180] for track '27' has 1 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
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