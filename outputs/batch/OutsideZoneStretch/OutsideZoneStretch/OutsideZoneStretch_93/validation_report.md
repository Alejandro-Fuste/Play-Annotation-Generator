# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_93`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_93/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 44 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 188: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PreSnap' range [0-111] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-133] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-294] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-284] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-65] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-70] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-244] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-154] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-248] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-58] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-84] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-179] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-191] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-299] for track '18' has 2 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.