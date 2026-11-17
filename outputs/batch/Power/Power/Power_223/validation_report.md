# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_223`
- **Input XML**: `outputs/batch/Power/Power/Power_223/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 53 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PreSnap' range [5-151] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-181] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-191] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-273] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-153] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-299] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-238] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-299] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-225] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-276] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-162] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-205] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-219] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-257] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-297] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-167] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [142-177] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-292] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-177] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-188] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-299] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-293] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-156] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-259] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-245] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-165] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [142-196] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [142-187] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-137] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-299] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-207] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-211] for track '24' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.