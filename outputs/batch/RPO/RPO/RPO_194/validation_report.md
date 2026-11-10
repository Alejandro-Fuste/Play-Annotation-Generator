# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `RPO_194`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_194/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 63 |
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
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-104] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-149] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-132] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-147] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-155] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-177] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-109] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-106] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-112] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-157] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-145] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-67] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-89] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-100] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-67] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-31] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-69] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-74] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-78] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-152] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-93] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-96] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-40] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-119] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-156] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-166] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-31] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-67] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-81] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-179] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-31] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-77] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-100] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-165] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-65] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-132] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-153] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-166] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-148] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-155] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-146] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-150] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-176] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-164] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-170] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-180] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-154] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-173] for track '25' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.