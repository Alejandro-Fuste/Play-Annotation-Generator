# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_175`
- **Input XML**: `outputs/batch/Power/Power/Power_175/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 70 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [25-300] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [315-320] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-315] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [322-324] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [327-329] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-215] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-329] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-185] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-189] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-222] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-145] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-152] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-169] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-172] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [139-189] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-205] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-329] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-181] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-187] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-196] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-206] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-235] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-153] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [139-167] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [180-181] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [139-146] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [148-153] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-329] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-43] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-135] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-194] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-296] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [306-307] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [309-329] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-52] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-70] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-227] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-257] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-193] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-215] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-235] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-248] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-240] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-248] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-329] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-262] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-329] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-266] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [281-282] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-285] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [280-285] for track '30' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.