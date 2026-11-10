# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_158`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_158/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 74 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_RunBlock' for track '16' has invalid range: start=45, end=43. Clamping end to start.
> - Action 'Action_None' range [44-176] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-151] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-180] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [44-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [45-53] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [56-57] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-98] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-98] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-101] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-96] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-173] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PullBall' range [68-70] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [45-58] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [70-90] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-110] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-71] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-90] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-106] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [45-54] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-96] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-34] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-64] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [67-68] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-75] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [79-94] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-43] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-50] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-72] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [78-80] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-87] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-101] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-98] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [101-102] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-116] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-100] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-160] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-180] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [153-154] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-180] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-180] for track '25' has 1 frames without a visible bounding box.
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
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.