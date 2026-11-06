# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_14`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_14/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 72 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_PreSnap' range [0-262] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-144] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-263] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-105] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-162] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-167] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-208] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-233] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-269] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-112] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [83-100] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '10' starts at frame 126, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [126-126] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-269] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-89] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-116] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-122] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-243] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-79] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-160] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-175] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-188] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-118] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-98] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-107] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-79] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-122] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-164] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-269] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-236] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-266] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-227] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-269] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-269] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-169] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-269] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-215] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-224] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-232] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-237] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-247] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-165] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-265] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-249] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-269] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-228] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-233] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-239] for track '29' has 1 frames without a visible bounding box.
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
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.