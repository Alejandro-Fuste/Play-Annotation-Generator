# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_109`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_109/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 58 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_PreSnap' range [0-95] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-122] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [78-113] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [120-121] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-114] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-140] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-134] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-159] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-184] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-269] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [78-125] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-129] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [78-90] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [92-94] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-218] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-97] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-91] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-124] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-128] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-136] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-77] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [82-100] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-230] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-262] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-248] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-212] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-262] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-246] for track '25' has 1 frames without a visible bounding box.
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
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.