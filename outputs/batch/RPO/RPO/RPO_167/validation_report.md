# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `RPO_167`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_167/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 55 |
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
> - Action 'Action_PreSnap' range [5-207] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-76] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-107] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-56] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-80] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-116] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-94] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-99] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-160] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-189] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-200] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-145] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-210] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-188] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-182] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-210] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-210] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-70] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-210] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-90] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-40] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-64] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-210] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-9] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-27] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-71] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-120] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-162] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-204] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-156] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-181] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-135] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-165] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-175] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-202] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-206] for track '25' has 1 frames without a visible bounding box.
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