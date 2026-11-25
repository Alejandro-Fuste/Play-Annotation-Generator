# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_177`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_177/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 64 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '4' has invalid range: start=183, end=135. Clamping end to start.
> - Segment 'Action_ZoneBlock' for track '8' has invalid range: start=183, end=136. Clamping end to start.
> - Segment 'Action_ZoneBlock' for track '11' has invalid range: start=183, end=129. Clamping end to start.
> - Segment 'Action_ZoneBlock' for track '12' has invalid range: start=183, end=119. Clamping end to start.
> - Segment 'Action_BallSnap' for track '13' has invalid range: start=180, end=127. Clamping end to start.
> - Segment 'Action_ZoneBlock' for track '13' has invalid range: start=183, end=127. Clamping end to start.
> - Segment 'Action_SnapReceive' for track '16' has invalid range: start=180, end=111. Clamping end to start.
> - Segment 'Action_ReadDefender' for track '16' has invalid range: start=195, end=111. Clamping end to start.
> - Segment 'Action_Handoff' for track '16' has invalid range: start=212, end=111. Clamping end to start.
> - Segment 'Action_BallCarry' for track '16' has invalid range: start=223, end=111. Clamping end to start.
> - Action 'Action_PreSnap' range [0-140] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-200] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-252] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [256-260] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-268] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-299] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-192] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-196] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-200] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-89] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-121] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-135] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-127] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-132] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-136] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-62] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-136] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-142] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-11] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-72] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-76] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-89] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-129] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-89] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-119] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-127] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-87] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-126] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-105] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-111] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-191] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-156] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-280] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-190] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [189-299] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-213] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [217-218] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-226] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-263] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-273] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [276-283] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [236-255] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-258] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-267] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [271-279] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [281-283] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-246] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-251] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-254] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-267] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [281-284] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-271] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-276] for track '33' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_177'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.