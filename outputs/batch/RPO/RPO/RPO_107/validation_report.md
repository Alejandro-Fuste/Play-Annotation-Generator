# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_107`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_107/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 96 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '21' has invalid range: start=77, end=69. Clamping end to start.
> - Action 'Action_None' range [76-221] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [227-238] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [245-269] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-119] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-137] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-148] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-71] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [76-79] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-157] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [76-87] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-141] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [143-251] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [76-269] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-43] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [76-100] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [106-269] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-50] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-80] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-90] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-100] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [102-109] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-197] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-94] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-98] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-110] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-75] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [83-205] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-139] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-40] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-134] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-214] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-38] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-74] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [83-140] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-205] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-165] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [83-92] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-187] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-28] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-40] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-69] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-84] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-228] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [100-146] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-119] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-252] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-123] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-222] for track '26' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [138-139] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-246] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [152-158] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-170] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-210] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [212-214] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-218] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-223] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-163] for track '29' has 2 frames without a visible bounding box.
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
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.