# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_285`
- **Input XML**: `outputs/batch/Power/Power/Power_285/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 53 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 570: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
> - Row 570: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_PreSnap' range [25-182] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-193] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-257] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [142-216] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-193] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-251] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-171] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-214] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-158] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-174] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-189] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [142-169] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [190-191] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [194-196] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-263] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [142-199] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [201-202] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [205-206] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-199] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-207] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-246] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [142-209] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-172] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-269] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-186] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-233] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-241] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-269] for track '26' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
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