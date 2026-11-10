# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_105`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_105/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 40 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [12-200] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-215] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-187] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-170] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-182] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-239] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-168] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-193] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-200] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-227] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-233] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [218-220] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-239] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-239] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [194-215] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-212] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-219] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-233] for track '23' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.