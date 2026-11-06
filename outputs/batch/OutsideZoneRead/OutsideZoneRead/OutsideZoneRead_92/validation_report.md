# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_92`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_92/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 92 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-239] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-182] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-188] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-239] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-97] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-106] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-111] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-124] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-85] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-96] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-108] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-238] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [51-84] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [86-93] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [97-130] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-196] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-200] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-203] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-221] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-226] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-229] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [57-73] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-189] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-217] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-239] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-196] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [51-75] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [91-130] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-132] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [51-99] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [111-123] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-153] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [205-211] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-221] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-239] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-92] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-40] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-51] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-109] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-11] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-26] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-239] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-164] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-239] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-144] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-176] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-187] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-192] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-199] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-217] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-227] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-189] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-200] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-204] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-181] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-200] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-214] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-221] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-228] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-211] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-239] for track '34' has 2 frames without a visible bounding box.
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
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.