# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_92`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_92/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 60 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 186: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action 'Action_PreSnap' range [0-161] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-264] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-359] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-234] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-242] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-285] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-208] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-250] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-265] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-179] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-258] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [111-135] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [111-136] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [147-151] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [153-160] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-166] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-175] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-178] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-266] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-271] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-282] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-359] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-207] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-356] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-278] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [111-138] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [151-154] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-255] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-273] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-359] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-359] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-146] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-177] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-275] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-147] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-331] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-174] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-253] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-207] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-256] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-247] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-252] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-258] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-299] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [270-308] for track '28' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.