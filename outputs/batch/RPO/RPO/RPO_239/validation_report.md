# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `RPO_239`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_239/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 62 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - RPO Run Block requires exactly five verified OL positions ['C', 'LG', 'LT', 'RG', 'RT']; found ['C', 'LG', 'LT', 'RT'].

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-233] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-225] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-230] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-239] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-128] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-99] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-113] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-161] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-151] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-65] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-157] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [86-239] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-115] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-168] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-156] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-66] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-126] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-135] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-66] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-100] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-134] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-145] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-177] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-123] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-154] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-75] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-37] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-114] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-78] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-110] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-123] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-189] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-56] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-62] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-99] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-113] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-166] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-148] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-137] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-145] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-150] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-173] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-239] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-136] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-146] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-161] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-160] for track '27' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-144] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-173] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-183] for track '30' has 1 frames without a visible bounding box.
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
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.