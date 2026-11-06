# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_52`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_52/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 31 |
| Ball Tracks | 2 |
| CSV events parsed | 18 |
| Action Segments inferred | 64 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-99] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [72-91] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-191] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' for track '4' starts at frame 67, but the player has no visible bounding box on this frame.
> - Action 'Action_ZoneBlock' range [67-67] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-239] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-126] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-209] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-93] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-93] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-214] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-86] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-223] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-156] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-234] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-84] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-69] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-46] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-50] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-57] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-64] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-70] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-117] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-105] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-152] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-151] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-239] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-161] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-172] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-200] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-239] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-171] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-185] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-204] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-236] for track '31' has 1 frames without a visible bounding box.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.