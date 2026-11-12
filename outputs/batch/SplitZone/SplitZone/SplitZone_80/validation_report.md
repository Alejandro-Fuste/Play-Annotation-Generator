# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_80`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_80/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 41 |
| Player Tracks | 41 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 118 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 539 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '1' (RG) duration 110 frames exceeds threshold 90 frames [start=315, end=424].
> - Validation warning: Action 'Action_ZoneBlock' for track '2' (LT) duration 95 frames exceeds threshold 90 frames [start=315, end=409].
> - Validation warning: Action 'Action_ZoneBlock' for track '5' (RT) duration 110 frames exceeds threshold 90 frames [start=315, end=424].
> - Validation warning: Action 'Action_ZoneBlock' for track '14' (C) duration 110 frames exceeds threshold 90 frames [start=315, end=424].
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [312–319], lower_priority='Action_ZoneBlock' annotated_start=315, effective_Action_ZoneBlock_start=320.
> - Action 'Action_PreSnap' range [19-141] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-338] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [340-382] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [444-448] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-128] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [425-463] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-168] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [315-402] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [404-409] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-314] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [318-424] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [425-483] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-393] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-112] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [425-451] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [330-354] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [358-475] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [312-354] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [312-332] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-415] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [419-426] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-470] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-134] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-233] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-111] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-122] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-85] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-122] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-137] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-144] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-212] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [273-301] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [305-306] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [341-342] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [377-384] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [391-392] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [425-445] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-489] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [491-492] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-81] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-124] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-126] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-186] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-197] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-201] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-217] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-263] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-311] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-349] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [351-393] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-480] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [312-366] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [371-375] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [377-529] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [533-538] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [305-306] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-316] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-446] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [448-465] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-388] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [391-452] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [462-487] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [490-539] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [361-378] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [383-385] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-537] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [405-412] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [414-422] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [405-441] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [448-487] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [489-539] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [407-420] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [426-434] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [442-443] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [448-450] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [463-464] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [471-498] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [413-473] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [420-502] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [421-487] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [448-451] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [469-471] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [453-475] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [475-476] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [476-482] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [492-503] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [511-516] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [496-498] for track '36' has 1 frames without a visible bounding box.
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
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.