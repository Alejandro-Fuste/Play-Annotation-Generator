# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_311`
- **Input XML**: `outputs/batch/Power/Power/Power_311/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 58 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 622: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [11-239] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-217] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-239] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-219] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-226] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-211] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-218] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-167] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-206] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-239] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-239] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-201] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-154] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [142-149] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [157-158] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [162-166] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-211] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-223] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-161] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-173] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-162] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-171] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [142-145] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [148-160] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [162-181] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [186-187] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-197] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-38] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-239] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-195] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-224] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-228] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-207] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-222] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-226] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-233] for track '28' has 1 frames without a visible bounding box.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
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