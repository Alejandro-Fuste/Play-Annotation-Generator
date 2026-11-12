# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_213`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_213/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 118 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 479 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Track ID '23' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '0' (RT) duration 166 frames exceeds threshold 90 frames [start=235, end=400].
> - Segment 'Action_SnapReceive' for track '10' has invalid range: start=233, end=226. Clamping end to start.
> - Validation warning: Action 'Action_BlockSecondLevel' for track '12' (SAF1) duration 135 frames exceeds threshold 90 frames [start=266, end=400].
> - Validation warning: Action 'Action_ZoneBlock' for track '13' (C) duration 166 frames exceeds threshold 90 frames [start=235, end=400].
> - Segment 'Action_BallSnap' for track '16' has invalid range: start=233, end=226. Clamping end to start.
> - Validation warning: Action 'Action_ZoneBlock' for track '17' (LG) duration 128 frames exceeds threshold 90 frames [start=235, end=362].
> - Validation warning: Action 'Action_ZoneBlock' for track '18' (RG) duration 166 frames exceeds threshold 90 frames [start=235, end=400].
> - Validation warning: Action 'Action_ZoneBlock' for track '19' (LT) duration 166 frames exceeds threshold 90 frames [start=235, end=400].
> - Action 'Action_BallCarry' range [266-479] for track '1' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-80] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-310] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-336] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [233-479] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [233-352] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-448] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-326] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [332-334] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-342] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-350] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [355-356] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-369] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-479] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-307] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [326-330] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-479] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [239-302] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [306-340] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-254] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-369] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [233-479] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [266-400] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [401-420] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [423-424] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [426-474] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [235-366] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [233-363] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [367-368] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [370-391] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-252] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-289] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-281] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-306] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [309-310] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-315] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-38] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [235-353] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [359-362] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [235-349] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [359-400] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [235-279] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [285-290] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [292-295] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [301-302] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [304-311] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [314-356] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [367-368] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [374-392] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [394-395] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '19' starts at frame 401, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [401-415] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [420-421] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [423-479] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-27] for track '21' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-35] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [233-356] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [358-369] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [374-377] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [379-414] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-287] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-291] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-298] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [301-324] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [338-340] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-346] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-479] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-369] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [363-371] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [383-406] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [395-399] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [402-404] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [408-409] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [411-412] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [432-479] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [451-453] for track '31' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.