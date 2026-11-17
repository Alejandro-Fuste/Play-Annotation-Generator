# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_309`
- **Input XML**: `outputs/batch/Power/Power/Power_309/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 54 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 617: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - Row 618: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [22-187] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-220] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-128] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-207] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-133] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-138] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [96-103] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [111-115] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-231] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-239] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-109] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-124] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-127] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-111] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-115] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-124] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-175] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-189] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-205] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-216] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-231] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-146] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-193] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-239] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-224] for track '25' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
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