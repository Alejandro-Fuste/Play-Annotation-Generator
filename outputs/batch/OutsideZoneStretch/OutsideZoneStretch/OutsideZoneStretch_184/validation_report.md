# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_184`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_184/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 85 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-152] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-157] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PressEdge' for track '2' starts at frame 73, but the player has no visible bounding box on this frame.
> - Action 'Action_PressEdge' range [73-73] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-121] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-138] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-163] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [166-207] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-218] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [225-231] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [233-234] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-167] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-96] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-160] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-199] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-183] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-58] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-118] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-181] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-188] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-209] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-225] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-127] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-139] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-149] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-160] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-206] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [37-50] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [57-71] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [74-78] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-209] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [79-108] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-114] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-129] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-187] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-99] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-104] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-172] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-175] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-56] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-33] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [47-68] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-107] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-116] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-139] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-147] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-168] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-183] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-187] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-202] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [37-41] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-92] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-89] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-109] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-126] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-69] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-107] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-168] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-196] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-16] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-33] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-76] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-117] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-217] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-95] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-193] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-137] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-175] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-199] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-163] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-191] for track '29' has 1 frames without a visible bounding box.
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