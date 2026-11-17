# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_74`
- **Input XML**: `outputs/batch/Power/Power/Power_74/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 64 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PreSnap' range [6-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-262] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-197] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-159] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-162] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-176] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-88] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-201] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-119] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-134] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-199] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-107] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-117] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-130] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-137] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-152] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-167] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-162] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-109] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-149] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-204] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-203] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-38] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-43] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-49] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-56] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-70] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-299] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-215] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-208] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-260] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-299] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [90-118] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-25] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-31] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-35] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-113] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-156] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-168] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-176] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-28] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-34] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-118] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-152] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-171] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-99] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-106] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-127] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-209] for track '19' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-192] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-212] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-206] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-216] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-208] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-230] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-258] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-263] for track '27' has 1 frames without a visible bounding box.
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
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.